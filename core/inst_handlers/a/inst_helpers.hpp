#pragma once
#include "core/AtlasState.hpp"
#include "core/AtlasInst.hpp"
#include "include/AtlasUtils.hpp"

namespace atlas
{
    class ActionGroup;

    using W = uint32_t;
    using D = uint64_t;

    template <typename T> ActionGroup* compute_address_handler(AtlasState* state)
    {
        static_assert(std::is_same_v<T, RV64> || std::is_same_v<T, RV32>);

        const AtlasInstPtr & inst = state->getCurrentInst();
        const T rs1_val = inst->getRs1Reg()->dmiRead<uint64_t>();
        constexpr uint32_t IMM_SIZE = 12;
        const T imm = inst->hasImmediate() ? inst->getSignExtendedImmediate<T, IMM_SIZE>() : 0;
        const T vaddr = rs1_val + imm;
        state->getTranslationState()->makeTranslationRequest(vaddr, sizeof(T));
        return nullptr;
    }

    template <typename RV, typename SIZE, template <typename> class BinaryOp, bool U = true>
    ActionGroup* amo_handler(atlas::AtlasState* state)
    {
        static_assert(std::is_same_v<RV, RV64> || std::is_same_v<RV, RV32>);
        static_assert(std::is_same_v<SIZE, W> || std::is_same_v<SIZE, D>);
        static_assert(sizeof(RV) >= sizeof(SIZE));

        using Op =
            typename std::conditional<std::is_same_v<RV, RV64>,
                                      typename std::conditional<U, uint64_t, int64_t>::type,
                                      typename std::conditional<U, uint32_t, int32_t>::type>::type;

        BinaryOp<Op> binary_op;
        const AtlasInstPtr & inst = state->getCurrentInst();
        const RV paddr = state->getTranslationState()->getTranslationResult().getPaddr();
        RV rd_val = 0;
        if constexpr (sizeof(RV) > sizeof(SIZE))
        {
            rd_val = signExtend<SIZE, RV>(state->readMemory<SIZE>(paddr));
        }
        else
        {
            rd_val = state->readMemory<SIZE>(paddr);
        }
        inst->getRdReg()->write(rd_val);
        const RV rs2_val = inst->getRs2Reg()->dmiRead<uint64_t>();
        state->writeMemory<SIZE>(paddr, binary_op(rd_val, rs2_val));
        return nullptr;
    }

    template <typename T> struct MaxFunctor
    {
        constexpr T operator()(const T & lhs, const T & rhs) const { return lhs > rhs ? lhs : rhs; }
    };

    template <typename T> struct MinFunctor
    {
        constexpr T operator()(const T & lhs, const T & rhs) const { return lhs > rhs ? rhs : lhs; }
    };

    template <typename T> struct SwapFunctor
    {
        constexpr T operator()(const T & lhs, const T & rhs) const
        {
            (void)lhs;
            return rhs;
        }
    };
} // namespace atlas
