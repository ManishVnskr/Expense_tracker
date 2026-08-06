package com.expensetracker.service;

import com.expensetracker.dto.TransactionRequest;
import com.expensetracker.model.Transaction;
import com.expensetracker.repository.TransactionRepository;
import jakarta.persistence.criteria.Predicate;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Service
public class TransactionService {

    private final TransactionRepository transactionRepository;
    private final UserService userService;

    public TransactionService(TransactionRepository transactionRepository, UserService userService) {
        this.transactionRepository = transactionRepository;
        this.userService = userService;
    }

    public Page<Transaction> getTransactions(Long householdId, LocalDate startDate, LocalDate endDate,
                                              Long categoryId, Transaction.TransactionType type,
                                              String paymentMethod, String search,
                                              int page, int size) {
        userService.validateHouseholdAccess(householdId);
        
        Pageable pageable = PageRequest.of(page, size, Sort.by(Sort.Direction.DESC, "transactionDate", "id"));
        
        Specification<Transaction> spec = (root, query, cb) -> {
            List<Predicate> predicates = new ArrayList<>();
            predicates.add(cb.equal(root.get("householdId"), householdId));
            
            if (startDate != null) {
                predicates.add(cb.greaterThanOrEqualTo(root.get("transactionDate"), startDate));
            }
            if (endDate != null) {
                predicates.add(cb.lessThanOrEqualTo(root.get("transactionDate"), endDate));
            }
            if (categoryId != null) {
                predicates.add(cb.equal(root.get("categoryId"), categoryId));
            }
            if (type != null) {
                predicates.add(cb.equal(root.get("type"), type));
            }
            if (paymentMethod != null && !paymentMethod.isEmpty()) {
                predicates.add(cb.equal(root.get("paymentMethod"), paymentMethod));
            }
            if (search != null && !search.isEmpty()) {
                predicates.add(cb.like(cb.lower(root.get("description")), "%" + search.toLowerCase() + "%"));
            }
            
            return cb.and(predicates.toArray(new Predicate[0]));
        };
        
        return transactionRepository.findAll(spec, pageable);
    }

    @Transactional
    public Transaction createTransaction(Long householdId, TransactionRequest request) {
        userService.validateHouseholdAccess(householdId);
        
        Transaction transaction = Transaction.builder()
                .householdId(householdId)
                .categoryId(request.getCategoryId())
                .amount(request.getAmount())
                .type(request.getType())
                .description(request.getDescription())
                .transactionDate(request.getTransactionDate())
                .paymentMethod(request.getPaymentMethod())
                .tags(request.getTags())
                .build();
        
        return transactionRepository.save(transaction);
    }

    @Transactional
    public Transaction updateTransaction(Long householdId, Long transactionId, TransactionRequest request) {
        userService.validateHouseholdAccess(householdId);
        
        Transaction transaction = transactionRepository.findById(transactionId)
                .orElseThrow(() -> new RuntimeException("Transaction not found"));
        
        if (!transaction.getHouseholdId().equals(householdId)) {
            throw new RuntimeException("Access denied");
        }
        
        transaction.setAmount(request.getAmount());
        transaction.setType(request.getType());
        transaction.setCategoryId(request.getCategoryId());
        transaction.setDescription(request.getDescription());
        transaction.setTransactionDate(request.getTransactionDate());
        transaction.setPaymentMethod(request.getPaymentMethod());
        transaction.setTags(request.getTags());
        
        return transactionRepository.save(transaction);
    }

    @Transactional
    public void deleteTransaction(Long householdId, Long transactionId) {
        userService.validateHouseholdAccess(householdId);
        
        Transaction transaction = transactionRepository.findById(transactionId)
                .orElseThrow(() -> new RuntimeException("Transaction not found"));
        
        if (!transaction.getHouseholdId().equals(householdId)) {
            throw new RuntimeException("Access denied");
        }
        
        transactionRepository.deleteById(transactionId);
    }

    @Transactional
    public void bulkDeleteTransactions(Long householdId, List<Long> transactionIds) {
        userService.validateHouseholdAccess(householdId);
        
        List<Transaction> transactions = transactionRepository.findAllById(transactionIds);
        
        // Verify all transactions belong to this household
        for (Transaction transaction : transactions) {
            if (!transaction.getHouseholdId().equals(householdId)) {
                throw new RuntimeException("Access denied: Some transactions don't belong to this household");
            }
        }
        
        transactionRepository.deleteAllById(transactionIds);
    }
}
